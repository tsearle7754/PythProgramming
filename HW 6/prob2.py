from pathlib import Path

def compare_dirs(dirA, dirB):
    pathA = Path(dirA)
    pathB = Path(dirB)
    
    filesA = {f.name for f in pathA.iterdir() if f.is_file()}
    filesB = {f.name for f in pathB.iterdir() if f.is_file()}
    
    onlyA = sorted(filesA - filesB)
    onlyB = sorted(filesB - filesA)
    common = sorted(filesA & filesB)
    
    report_lines = [
        "FILES ONLY IN A:",
        *onlyA,
        "",
        "FILES ONLY IN B:",
        *onlyB,
        "",
        "FILES IN BOTH:",
        *common,
    ]
    
    with open("diff_report.txt", "w") as f:
        for line in report_lines:
            f.write(line + "\n")
            
    print("Report saved to diff_report.txt")