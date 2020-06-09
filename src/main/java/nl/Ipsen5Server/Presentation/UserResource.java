package nl.Ipsen5Server.Presentation;

import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;
import nl.Ipsen5Server.Domain.Dump;
import nl.Ipsen5Server.Domain.TokenBody;
import nl.Ipsen5Server.Domain.User;
import nl.Ipsen5Server.Interfaces.Authorisation;
import nl.Ipsen5Server.Service.Token;

import org.jdbi.v3.core.Jdbi;
import org.joda.time.LocalDateTime;
import org.json.JSONObject;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import java.util.*;

@Path("/user")
public class UserResource {

    private UserDAO dao;
    private Authorisation tokenUtils; 
    private String failedResponeMessage = "Login credentials were invalide";    
    private Response defaultRespone = Response.serverError()
            .entity(failedResponeMessage)
            .build();
  
    
    public UserResource(UserDAO dao, Authorisation tokenUtils) {
		super();
		this.dao = dao;
		this.tokenUtils = tokenUtils;
	}


	@GET
    public List<User> getAll() { return dao.getAll(); }


    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getAllUsers() {
        ArrayList<User> allUsers = dao.getAll();

        if (allUsers == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(allUsers, MediaType.APPLICATION_JSON).build();
    }


    @GET
    @Produces(MediaType.APPLICATION_JSON)
    @Path("/id/{Email}")
    public Response findUserById(@PathParam("Email") String Email) {
        User user = dao.getUserByEmail(Email);

        if (user == null) {
            throw new WebApplicationException(Response.Status.NOT_FOUND);
        }

        return Response.ok(user, MediaType.APPLICATION_JSON).build();
    }


    @POST
    @Path("/delete")
    public Response deleteUser(
        @FormParam("Email") String Email
    ){
        dao.deleteByEmail(Email);

        return Response.ok()
                .entity("Deleted account with email: ' " + Email + " '  successfully")
                .build();
    }
    
    
    
    @PUT
    @Path("/{token}/password")
    public Response passwordUser(
    		
    		@PathParam("token") String token,
    		Account user2
    		
    ){
    	Response response = defaultRespone;
    	
    	
    	try {
    		
    		
    		
    		String Email  = "Email";
    		String UserPassword= "UserPassword";
    			
    		String NewPassword= user2.getUserPassword();
    		  
    		  
    			Map<String, String> h = tokenUtils.decrypt(token)	;
    			
    					
    					  String Email2 = h.get(Email);		
    					  String UserPassword2 = h.get(UserPassword);
    		
    			tokenUtils.check(new Account(Email2, UserPassword2), dao);
    		
    			 new Thread(() -> {
    		
    		    		dao.changePassword(Email2, UserPassword2, NewPassword );
    		 
    			   	}).start();
    		
    		String message = "Successfull"; 
    		
    		Response successResponse = Response.ok(message)                      
    	            .build();
    		
    		response = successResponse; //change response 
    		
    		
    		}
    		catch (NotAuthorizedException e) {
    		
    		}
    		        
    		
    		return response;
        
        
        
        
    }
    
    
    /**
    *
    * @author Anthony Scheeres
    *
    */
    
    
    
    
    /**
    *
    * @author Anthony Scheeres
    *
    */
    @POST
    @Path("/login")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response loginUser(
    		Account user
    ){	
    	//define default response return when error
    	String failedResponeMessage = "Login credentials were invalide";
    	
    	Response defaultRespone = Response.serverError()
                .entity(failedResponeMessage)
                .build();
    	
    	Response response = defaultRespone; //return this response unless changed
    	
try {
	
	tokenUtils.check(user , dao);
	
	
	
	
String token = tokenUtils.create(user);
	
	Response successResponse = Response.ok(new TokenBody(token), MediaType.APPLICATION_JSON)                       //Initialize success response and pass the token
       
            .build();
	
	response = successResponse; //change response 

}
catch (NotAuthorizedException e) {
	//do something different or customize the response 
}
        	
        	

        	
        
        
        return response;
    }

}
