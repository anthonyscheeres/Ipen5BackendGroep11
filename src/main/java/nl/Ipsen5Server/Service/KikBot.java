package nl.Ipsen5Server.Service;

import ch.qos.logback.core.net.SyslogOutputStream;
import nl.Ipsen5Server.Interfaces.Platform;

import java.io.*;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.FileWriter;

/**
*
* @author Anthony Scheeres
*
*/
public class KikBot implements Platform{
   
	
	public List<String> usernames = new ArrayList<String>(); 
	
	public String platformName = "kik";

	@Override
	public void send(String message, List<String> users) {

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
	
	
	public List<String> getUsernames() {
		return usernames;
	}




	public void setUsernames(List<String> usernames) {
		this.usernames = usernames;
	}




	public String getPlatformName() {
		return platformName;
	}




	public void setPlatformName(String platformName) {
		this.platformName = platformName;
	}
	
	

}
