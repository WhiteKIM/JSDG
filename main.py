from parser.DataGenerator import Genernator
import json
from pathlib import Path

if __name__ == '__main__':
  '''
    추가적으로 여러 파일을 생성할 수 있도록 구성해야하고
    INPUT 파일명과 OUTPUT 파일명을 동일하게 구성
  '''
  modelFolder = Path('./model')
  inputFileList = [file.name for file in modelFolder.iterdir() if file.is_file()]

  # 파일 시작 진입점
  for inputFile in inputFileList:
    with open(f"./model/{inputFile}", 'r', encoding='utf-8') as jsonFile:
      jsonList = Genernator.generatingSampleData(json.load(jsonFile))
      print(jsonList)

      with open(f"./output/{inputFile}", 'w', encoding='utf-8') as outputFile:
        json.dump(jsonList, outputFile, ensure_ascii=False, indent='\t')
  