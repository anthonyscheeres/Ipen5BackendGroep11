package nl.Ipsen5Server.Presentation;

import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;

import javax.ws.rs.Consumes;
import javax.ws.rs.NotAuthorizedException;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.jdbi.v3.core.Jdbi;

import helpers.StringUtils;
import nl.Ipsen5Server.Data.BatchDAO;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;
import nl.Ipsen5Server.Domain.Dump;
import nl.Ipsen5Server.Domain.TokenBody;
import nl.Ipsen5Server.Interfaces.Authorisation;
import nl.Ipsen5Server.Service.Token;

@Path("/batch")
public class BatchResource {
    private BatchDAO dao;
    private Authorisation tokenUtils;
    private UserDAO user; 
    private String failedResponeMessage = "Login credentials were invalide";
    
    
    private Response defaultRespone = Response.serverError()
            .entity(failedResponeMessage)
            .build();
	
	
    
    
    /**
    *
    * @author Anthony Scheeres
    *
    */
	public BatchResource(BatchDAO dao, Authorisation tokenUtils, UserDAO user) {
		super();
		this.dao = dao;
		this.tokenUtils = tokenUtils;
		this.user = user;
	} 
  
	
	   /**
    *
    * @author Anthony Scheeres
    *
    */
    @POST
    @Path("/{token}/upload")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.TEXT_PLAIN)
public Response uploadDump(Dump[] excel, @PathParam("token") String token) {
	Response response = defaultRespone; //return this response unless changed
	
	
	try {
	
	String Email  = "Email";
	String UserPassword= "UserPassword";
		
	
	  
	  
		Map<String, String> h = tokenUtils.decrypt(token)	;
		
				
				  Email = h.get(Email);		
				  UserPassword = h.get(UserPassword);
	
		tokenUtils.check(new Account(Email, UserPassword), user);
		
	
		
		
		 new Thread(() -> {
	     	
			String batch = Base64.getEncoder().encodeToString(excel.toString().getBytes());
			
			batch = batch.substring(0, Math.min(batch.length(), 254)); //trim the string in case it gets to long for the database
			
			dao.InsertBatch(batch);
			
			
			
		
	for (Dump excelRow : excel) {
		
		dao.InsertPlatform(
				
				excelRow.getGenoemde_social_media()
				
				);
		
		dao.InsertContactPersoon(
				
				excelRow.getGenoemde_social_media(), 
				excelRow.getMessage(), 
				excelRow.getUser());
		
		dao.InsertContact(
				
				excelRow.getGenoemde_social_media(), 
				excelRow.getUser()
				
				);
		
		dao.UpdateInfo(
				
				excelRow.getPartial_IP(),
				excelRow.getMessage()
				
				);
		
		dao.InsertContactBatch(excelRow.getUser(), excelRow.getGenoemde_social_media()
				, batch);
		
		
	}
	
		   	}).start();
	
	String message = "Successfully created"; 
	
	Response successResponse = Response.ok(message)                       //Initialize success response and pass the token
            .build();
	
	response = successResponse; //change response 
	
	
	}
	catch (NotAuthorizedException e) {
	
	}
	        
	
	
	
		return response ;
	}
    
}
