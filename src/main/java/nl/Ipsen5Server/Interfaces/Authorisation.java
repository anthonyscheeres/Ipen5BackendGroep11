package nl.Ipsen5Server.Interfaces;

import java.util.HashMap;
import java.util.Map;

import javax.ws.rs.NotAuthorizedException;

import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;



/**
*
* @author Anthony Scheeres
*
*/
public interface Authorisation {
 
	
	String create(Account user);
	void check(Account user, UserDAO dao ) throws NotAuthorizedException;
	Map<String, String> decrypt(String token);
	
	
}
