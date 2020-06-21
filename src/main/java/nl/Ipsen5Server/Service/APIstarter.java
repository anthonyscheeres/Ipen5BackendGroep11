package nl.Ipsen5Server.Service;

import ch.qos.logback.core.net.SyslogOutputStream;

import java.io.*;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileWriter;


public class APIstarter {
    public APIstarter(){
        //sets up server
        try {
        String command = "python -m kik-bot-api-unofficial.examples";
        Process process = null;
        process = Runtime.getRuntime().exec(command);
        assert process != null;

        logOutput(process.getInputStream(), "");
        logOutput(process.getErrorStream(), "Error: ");

        //process.waitFor();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void SendMessageKik(String message, ArrayList<String> users)  {

        //writes users to file that will be read by API
        FileWriter fw= null;
        try {
            fw = new FileWriter("src\\main\\java\\nl\\Ipsen5Server\\Service\\users.txt");

            fw.write(users.toString());
            fw.close();

            //writes message to file that will be read by API
            FileWriter fw1 = new FileWriter("src\\main\\java\\nl\\Ipsen5Server\\Service\\message.txt");
            fw1.write(message);
            fw1.close();

            //creates client side and connects to API, this will trigger API to send the message to all users in users.txt file
            Socket s;
            s = new Socket(InetAddress.getLocalHost().getHostName(), 1234);
            PrintWriter pr = new PrintWriter(s.getOutputStream());
        }
        catch (IOException e) {
            e.printStackTrace();
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
