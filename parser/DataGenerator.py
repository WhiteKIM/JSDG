from lorem_text import lorem
import random

""" 
JSON Parser 구성

주어진 모델 JSON형식을 읽어서 데이터형식, 이름 등을 가져와야한다.
선구성된 JSON의 형식은 아래와 같다.

"keyName" : 'DATATYPE'

RESERVATION WORD
- DATATYPE : 데이터타입

"""

reversationWord = [
  'STRING',
  'INTEGER'
]

class Genernator:
  # 파싱된 key-value를 보고 샘플 데이터를 구성
  def generatingSampleData(data : dict):
    print(data)

    dataList = []
    jsonDict = {}

    for key, value in data.items():
      val = Genernator.__generatingSampleValue(value)
      jsonDict[key] = val
      
    dataList.append(jsonDict)

    return dataList


  # 타입에 해당하는 값을 구성하고 반환
  def __generatingSampleValue(val : str):
    words = Genernator.__parsing(val)
    result = ''

    # 순서대로 데이터타입이 주어진다.
    for word in words:
      if(word not in reversationWord):
        raise Exception('정의되지 않은 값입니다.')
      
      if(word == 'STRING'):
        result =  lorem.sentence()
      elif(word == 'INTEGER'):
        result = random.randint(1, 	2147483647)

    return result
  
  # 주어진 value를 공백문자를 기준으로 분리
  def __parsing(val : str):
    # 공백을 기준으로 값을 분리
    data = val.split(' ')

    return data
      
    