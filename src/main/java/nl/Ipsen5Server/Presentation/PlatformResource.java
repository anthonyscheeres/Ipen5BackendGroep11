package nl.Ipsen5Server.Presentation;

import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import nl.Ipsen5Server.Interfaces.Platform;
import nl.Ipsen5Server.Models.SocialMediaUsers;
import nl.Ipsen5Server.Service.KikBot;

@Path("/platform")
public class PlatformResource {
	
List<Platform> platforms;




	 public PlatformResource(List<Platform> platforms) {
	super();
	this.platforms = platforms;
}




	/**
	  *
	  * @author Anthony Scheeres
	  *
	  */
	 @POST
	 @Path("/send/{message}")
	 @Produces(MediaType.APPLICATION_JSON)
	 public Response sendMessagesToPlatform(@PathParam("message") String message, List<SocialMediaUsers> users){
		  if (users == null) {
	            throw new WebApplicationException(Response.Status.NOT_FOUND);
	        }
		 
		  
		  new Thread(() -> {
		  
	 
		 for (Platform platform : platforms) {
		 for (SocialMediaUsers user : users ) {

			 if (user.getPlatform().toLowerCase().contains(platform.getPlatformName())) {
				 
				 List<String> usernames = platform.getUsernames();
				 
				 usernames.add(user.username);
				 
				 platform.setUsernames(usernames);
				 
			 }
			 
			 }
		 platform.send(message, platform.getUsernames());
		 }
		  
		  
		
		  
		  }).start();
		  
	        return Response.ok(users, MediaType.APPLICATION_JSON).build();
		 
	 }
	
	
	 
	 
	 
	
}
