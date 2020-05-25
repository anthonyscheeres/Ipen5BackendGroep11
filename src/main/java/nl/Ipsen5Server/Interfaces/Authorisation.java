package nl.Ipsen5Server.Interfaces;

import java.util.HashMap;
import java.util.Map;

import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;

public interface Authorisation {
 
	
	String create(Account user);
	void check(Account user, UserDAO dao );
	Map<String, Object> decrypt(String token);
	
	
}
