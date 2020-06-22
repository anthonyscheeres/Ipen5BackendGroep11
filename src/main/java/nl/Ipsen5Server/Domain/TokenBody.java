package nl.Ipsen5Server.Domain;

public class TokenBody {
	public String token;
public String role;



public TokenBody(String token, String role) {
	super();
	this.token = token;
	this.role = role;
}



public TokenBody(String token) {
	super();
	this.token = token;
}

	
	
	
}
