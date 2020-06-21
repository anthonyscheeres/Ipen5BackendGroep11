package nl.Ipsen5Server.Presentation;

import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import nl.Ipsen5Server.Models.SocialMediaUsers;
import nl.Ipsen5Server.Service.APIstarter;

@Path("/platform")
public class PlatformResource {
	
	private APIstarter kik;

	public PlatformResource(APIstarter kik) {
		super();
		this.kik = kik;
	}
	


	 /**
	  *
	  * @author Anthony Scheeres
	  *
	  */
	 @GET
	 @Path("/send/{message}")
	 @Produces(MediaType.APPLICATION_JSON)
	 public Response sendMessagesToPlatform(@PathParam("message") String message, List<SocialMediaUsers> users){
		  if (users == null) {
	            throw new WebApplicationException(Response.Status.NOT_FOUND);
	        }
		 
		  
		  new Thread(() -> {
		  
		 ArrayList<String> arrayOfUsernamesToMessageOnKik = new ArrayList<String>();
		 
		 
		 for(SocialMediaUsers user : users ) {
			 
			 
			 if (user.getPlatform().toLowerCase().contains("kik")) {
				 
				 arrayOfUsernamesToMessageOnKik.add(user.getUsername()) ;
				 
			 }
			 
			 
		 }
		  
		  
		  this.kik.SendMessageKik(message, arrayOfUsernamesToMessageOnKik);
		  
		  }).start();
		  
	        return Response.ok(users, MediaType.APPLICATION_JSON).build();
		 
	 }
	
	
	
}
