package nl.Ipsen5Server.Presentation;

import javax.ws.rs.Path;

import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Interfaces.Authorisation;

@Path("/batch")
public class BatchResource {
    private UserDAO dao;
    private Authorisation tokenUtils;
    
	public BatchResource(UserDAO dao, Authorisation tokenUtils) {
		super();
		this.dao = dao;
		this.tokenUtils = tokenUtils;
	} 
    
    
    
}
