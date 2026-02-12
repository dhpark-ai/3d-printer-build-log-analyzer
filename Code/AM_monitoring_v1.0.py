# 본 코드는 V1.0 코드임.

import sys
import os
import re
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
import matplotlib.pyplot as plt

# 파라미터 기준
PARAMS = {
    'Actual temperature heating': (195, 205),
    'Residual oxygen value in module': (0, 0.3),
    'Dew point sensor': (-100, -20),
    'Process chamber left': (0, 60),
    'Process chamber right': (0, 60),
    'Ventilator rotation speed Bottom': (0, 79),
    'Differential pressure': (0, 70)
}

# 파라미터 패턴
PATTERNS = {
    'Residual oxygen value in module': r'Residual oxygen value in module:\s*([\d\.]+) ?%',
    'Ventilator rotation speed Bottom': r'Bottom\s*=\s*([\d\.]+) ?%',
    'Differential pressure': r'Differential pressure\s*:\s*([\d\.]+) ?mbar',
    'Actual temperature heating': r'Actual temperature heating\s*:\s*([\d\.]+) ?°?C',
    'Dew point sensor': r'Dew point sensor\s*:\s*(-?[\d\.]+) ?°?C',
    'Process chamber left': r'Process chamber left\s*:\s*([\d\.]+) ?°?C',
    'Process chamber right': r'Process chamber right\s*:\s*([\d\.]+) ?°?C'
}

class LogAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AM_Monitoring_v1.0')
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()
        self.label = QLabel('AM LOG 자동 분석기\n *문의 T.1493* ', self)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(self.label)

        self.button = QPushButton('로그 파일 선택', self)
        self.button.clicked.connect(self.select_file)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "로그 파일 선택", "", "Text Files (*.txt)")
        if file_path:
            try:
                result = self.analyze_log(file_path)
                QMessageBox.information(self, "분석 완료", f"분석 완료\n이상 항목: {result}건\noutput 폴더에서 결과를 확인하세요.")
            except Exception as e:
                QMessageBox.critical(self, "에러", f"에러 발생:\n{str(e)}")

    def analyze_log(self, file_path):
        results = {key: [] for key in PARAMS}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                time_match = re.match(r'([\d/]+ [\d:]+ [APM]+)', line)
                if not time_match:
                    continue
                try:
                    time_obj = datetime.strptime(time_match.group(1), '%m/%d/%Y %I:%M:%S %p')
                except:
                    continue
                for key, pattern in PATTERNS.items():
                    match = re.search(pattern, line)
                    if match:
                        try:
                            value = float(match.group(1))
                            results[key].append((time_obj, value))
                        except:
                            continue

        os.makedirs('output', exist_ok=True)
        warnings = []

        for param, data in results.items():
            if not data:
                continue
            times, values = zip(*data)
            low, high = PARAMS[param]

            plt.figure(figsize=(10, 4))
            plt.plot(times, values, label=param)
            plt.axhline(low, color='red', linestyle='--', label='Lower bound')
            plt.axhline(high, color='red', linestyle='--', label='Upper bound')
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.title(param)
            plt.legend()
            plt.tight_layout()
            plt.savefig(f'output/{param}.png')
            plt.close()

            for t, v in zip(times, values):
                if not (low <= v <= high):
                    warnings.append(f"[{t}] {param} - Out of range: {v}")

        with open('output/warnings.txt', 'w', encoding='utf-8') as wf:
            wf.write('\n'.join(warnings))

        return len(warnings)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogAnalyzer()
    window.show()
    sys.exit(app.exec_())
