print('Welcome to my computer quiz!')

playing = input('Do you want to play ? ')

if playing.lower() != 'yes':
	quit()

print("Okay Let's play :)")
score = 0

answer = input('What dose CPU stand for ? ')
if answer.lower() == 'central processing unit':
	print('correct')
	score += 1
else:
	print('incorrect')

answer = input('What dose GPU stand for ? ')
if answer.lower() == 'graphics processing unit':
	print('correct')
	score += 1
else:
	print('incorrect')

answer = input('What dose RAM stand for ? ')
if answer.lower() == 'random access memory':
	print('correct')
	score += 1
else:
	print('incorrect')

answer = input('What dose PSU stand for ? ')
if answer.lower() == 'power supply':
	print('correct')
	score += 1
else:
	print('incorrect')

print('You got '+str(score)+' question correct !')
print('You got '+str((score/4)*100)+'%')
