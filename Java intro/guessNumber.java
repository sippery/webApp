import javax.swing.JOptionPane;
public class guessNumber {
    public static void guessNumber(){
        int number = (int)(Math.random() * 100 + 1);
        String answer = JOptionPane.showInputDialog("Guess a number from 1-100");
        int answerInt = Integer.parseInt(answer);
        if (answerInt > number){
            JOptionPane.showMessageDialog(null, "You were higher than the correct answer.");
        }
        else if(answerInt < number){
            JOptionPane.showMessageDialog(null, "You were lower than the correct answer.");
        }
        else if(answerInt == number){
            JOptionPane.showMessageDialog(null, "Correct!");
        }
        while(answerInt != number){
            answer = JOptionPane.showInputDialog("Guess a number from 1-100");
            answerInt = Integer.parseInt(answer);
            if (answerInt > number){
                JOptionPane.showMessageDialog(null, "You were higher than the correct answer.");
            }
            else if(answerInt < number){
                JOptionPane.showMessageDialog(null, "You were lower than the correct answer.");
            }
            else if(answerInt == number){
                JOptionPane.showMessageDialog(null, "Correct!");
            }
        }
}
}   