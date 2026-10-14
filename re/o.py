# student ={ "name":"민지","scores":[80,70,90]}
# print(student["name"])
# student["scores"].append(100)
# average=sum(student["scores"])/len(student["scores"])
# print(f"{student["name"]}의 평균 : {average:.1f}점")

# total=sum([number for number in range(1,7) if number %2 !=0])
# print(total)
# scores = [55,80,70,95,60]
# i=0

# for score in scores:
#     if score>=70:
#         print(score)
#         i+=1

def check_pass_fail(scores):
    average = sum(scores) / len(scores)
    
    if average >= 70:
        return "합격"
    else:
        return "불합격"