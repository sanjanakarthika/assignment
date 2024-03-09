import json

def lambda_handler(event, context):
  str1 = event['str1'].lower()
  str2 = event['str2'].lower()

  if len(str1) != len(str2):
      return {
          'statusCode': 200,
          'body': json.dumps({'result': 'Not anagrams (lengths differ)'})
      }

  char_counts1 = {}
  char_counts2 = {}

  for char in str1:
      char_counts1[char] = char_counts1.get(char, 0) + 1

  for char in str2:
      char_counts2[char] = char_counts2.get(char, 0) + 1

  if char_counts1 == char_counts2:
      return {
          'statusCode': 200,
          'body': json.dumps({'result': 'Anagrams'})
      }
  else:
      return {
          'statusCode': 200,
          'body': json.dumps({'result': 'Not anagrams'})
      }

event = {
    'str1': 'listen',
    'str2': 'silent'
}

