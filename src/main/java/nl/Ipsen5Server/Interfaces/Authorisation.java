
package nl.Ipsen5Server.Interfaces;

import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;

import javax.ws.rs.NotAuthorizedException;
import java.util.Map;



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

