package nl.Ipsen5Server.Interfaces;

import nl.Ipsen5Server.Database.UserDAO;
import nl.Ipsen5Server.Domain.Account;

public interface Authorisation {
 
	
	public String create(Account user);
	public void check(Account user, UserDAO dao );
}
