**AI Number Guessing Game using the Minimax algorithm with Pygame:**



 *i. How to Run Your File:*



1.Save the code in a file named minimax\_guessing\_game.py.



2.Open your terminal or command prompt.



3.Navigate to the folder where the file is saved.



4.Run the game using:



(Bash)

python minimax\_guessing\_game.py



*ii. Required Software/Libraries*



You need the following installed:



Tool	         Purpose	             Install Command



Python 3.7+	Programming language	      Download Python



Pygame	        GUI and game rendering       pip install pygame





*iii. How to Play the Game:*



1.Think of a number between 1 and 100.



2.The AI will display a guess like:



"My guess is: 50"



3.You respond by clicking one of the buttons:



* High → if the guess is too high.



* Low → if the guess is too low.



* &nbsp;Correct → if the guess is right.



4\.The AI recalculates the next best guess using the Minimax algorithm.



5\.When you click “Correct,” the game ends and shows:



"Yay! I guessed it in X tries."





*iv. Algorithm Used:*



Minimax Algorithm



* The AI uses Minimax to simulate all possible outcomes.



* For each guess, it calculates the worst-case number of steps needed to find the correct number.



* It chooses the guess that minimizes the maximum number of steps.



* This is similar to how AI plays chess or tic-tac-toe, but adapted for number guessing.
