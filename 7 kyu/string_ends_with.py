def solution(string, ending):
  return True if string[-len(ending):] == ending or ending == '' else False
