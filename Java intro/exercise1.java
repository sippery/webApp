import javax.swing.JOptionPane;
public class exercise1{
    public static void exercise1(){

    int answer = JOptionPane.YES_NO_OPTION;
    Object[] options = { "True", "False" };
    
    answer = JOptionPane.showOptionDialog(null, "2 + 2 = 5", "True or False?",
    JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, 
    options, options[0]);

    while(answer == JOptionPane.YES_OPTION){
        answer = JOptionPane.showOptionDialog(null, "2 + 2 = 5", "True or False?",
        JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, 
        options, options[0]);
    }
    JOptionPane.showMessageDialog(null, "That is correct.", "Congratulations!", answer);
}
}