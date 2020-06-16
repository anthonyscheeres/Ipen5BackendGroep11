package nl.Ipsen5Server.Service;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileWriter;


public class APIstarter {
    public void SendMessageKik(String message, ArrayList<String> users) throws IOException, InterruptedException {

        FileWriter fw=new FileWriter("src\\main\\java\\nl\\Ipsen5Server\\Service\\users.txt");
        fw.write(users.toString());
        fw.close();

        FileWriter fw1=new FileWriter("src\\main\\java\\nl\\Ipsen5Server\\Service\\message.txt");
        fw1.write(message);
        fw1.close();

        Socket s;
        String command = "python -m kik-bot-api-unofficial.examples";

        Process process = Runtime.getRuntime().exec(command);
        logOutput(process.getInputStream(), "");
        logOutput(process.getErrorStream(), "Error: ");
        process.waitFor();

        {

            System.out.println("going to sleep");
            Thread.sleep(2000);
            System.out.println("waking up");

            s = new Socket("DESKTOP-5VQRO20",1234);
            //s = new Socket("127.0.0.1",1234);

            PrintWriter pr = new PrintWriter(s.getOutputStream());

        }

    }
    private void logOutput(InputStream inputStream, String prefix) {
        new Thread(() -> {
            Scanner scanner = new Scanner(inputStream, "UTF-8");
            while (scanner.hasNextLine()) {
                synchronized (this) {
                    System.out.println(prefix + scanner.nextLine());
                }
            }
            scanner.close();
        }).start();
    }
}
