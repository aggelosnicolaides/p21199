
with open("two_cities_ascii.txt", 'r+') as f:
   f = f.read()
total_binary = ''
def ascii_to_binary(text):
   total_binary = ''

   for i in range(len(text)):
      binary = ''
      string_ord = ord(text[i: i + 1])

      while string_ord > 0:
         x = string_ord % 2
         string_ord = string_ord // 2
         binary = str(x) + str(binary)
      total_binary += binary + ' '

   print(total_binary)

   return total_binary


ascii_to_binary(f)



def getMaxLength1(arr, n):

   count = 0

   result = 0

   for i in range(0, n):

      if (arr[i] == "0" or arr[i] == " "):
         count = 0

      else:

         count += 1
         result = max(result, count)

   return result

def getMaxLength0(arr, n):

   count0 = 0

   result0 = 0

   for i in range(0, n):

      if (arr[i] == "1" or arr[i] ==" "):
            count0 = 0

      else:

         count0 += 1
         result0 = max(result0, count0)

   return result0


arr = ascii_to_binary(f)
n = len(arr)
print("Τα περισσότερα συνεχόμενα 1 : ")
print(getMaxLength1(arr, n))
print("Τα περισσότερα συνεχόμενα 0 : ")
print(getMaxLength0(arr, n))
