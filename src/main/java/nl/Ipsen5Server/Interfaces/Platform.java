package nl.Ipsen5Server.Interfaces;

import java.util.ArrayList;
import java.util.List;


/**
*
* @author Anthony Scheeres
*
*/
public interface Platform {
	

	
	public void send(String message, List<String> users);
	

	public List<String> getUsernames() ;




	public void setUsernames(List<String> usernames) ;




	public String getPlatformName() ;




	public void setPlatformName(String platformName);
	
	

}
