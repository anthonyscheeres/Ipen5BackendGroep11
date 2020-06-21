package nl.Ipsen5Server.Presentation;


import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;
import nl.Ipsen5Server.Domain.TokenBody;
import nl.Ipsen5Server.Domain.User;
import nl.Ipsen5Server.Interfaces.Authorisation;



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


/* @GET
 public List < User > getAll() {
  return dao.getAll();
 }
*/

 
 
 @Path("/{token}")
 @GET
 @Produces(MediaType.APPLICATION_JSON)
 public Response getAllUsers( @PathParam("token") String token) {
 
	 
	 try {



		   String Email2 = "Email";
		   String UserPassword = "UserPassword";

		


		   Map < String, String > credentials = tokenUtils.decrypt(token);


		   String Email3 = credentials.get(Email2);
		   String UserPassword2 = credentials.get(UserPassword);

		   tokenUtils.check(new Account(Email3, UserPassword2), dao);
	  
	 
	 ArrayList < User > allUsers = dao.getAll();

  
  
  if (allUsers == null) {
   throw new WebApplicationException(Response.Status.NOT_FOUND);
  }

  return Response.ok(allUsers, MediaType.APPLICATION_JSON).build();
  
  
	  } catch (Exception e) {

	  }

	  return defaultRespone ;
  
 }


 @GET
 @Produces(MediaType.APPLICATION_JSON)
 @Path("/{token}/id/{Email}")
 public Response findUserById(
		 @PathParam("token") String token,
		 @PathParam("Email") String Email) {
 

  
  try {



	   String Email2 = "Email";
	   String UserPassword = "UserPassword";

	


	   Map < String, String > credentials = tokenUtils.decrypt(token);


	   String Email3 = credentials.get(Email2);
	   String UserPassword2 = credentials.get(UserPassword);

	   tokenUtils.check(new Account(Email3, UserPassword2), dao);
  
		 User user = dao.getUserByEmail(Email);
		  if (user == null) {
		   throw new WebApplicationException(Response.Status.NOT_FOUND);
		  }
	  
	   return Response.ok(user, MediaType.APPLICATION_JSON).build();
  
  } catch (Exception e) {

  }

  return defaultRespone ;
  
  
 }


 @POST
 @Path("/{token}/delete")
 public Response deleteUser(
		 @PathParam("token") String token,
  @FormParam("Email") String Email
 ) {
	 
	 
	 try {



		   String Email2 = "Email";
		   String UserPassword = "UserPassword";

		


		   Map < String, String > credentials = tokenUtils.decrypt(token);


		   String Email3 = credentials.get(Email2);
		   String UserPassword2 = credentials.get(UserPassword);

		   tokenUtils.check(new Account(Email3, UserPassword2), dao);
		   dao.deleteByEmail(Email);
  

		   return Response.ok()
				   .entity("Deleted account with email: ' " + Email + " '  successfully")
				   .build();
	 } catch (NotAuthorizedException e) {

	  }
	 return defaultRespone;

 }

 @POST
 @Path("/{token}/update")
 public Response updateUser(
		  @PathParam("token") String token,
  @FormParam("UserID") String UserID,
  @FormParam("ContactName") String ContactName,
  @FormParam("CustomMessage") String CustomMessage,
  @FormParam("Info") String Info

 ) {
	 
	 
	 try {



		   String Email = "Email";
		   String UserPassword = "UserPassword";

		


		   Map < String, String > credentials = tokenUtils.decrypt(token);


		   String Email2 = credentials.get(Email);
		   String UserPassword2 = credentials.get(UserPassword);

		   tokenUtils.check(new Account(Email2, UserPassword2), dao);

	 
	 
		   dao.updateByUsername(UserID, ContactName, CustomMessage, Info);

  
  
  
		   return Response.ok()
				   .entity("Updated Account with userid: ' " + UserID + " '  successfully")
				   .build();
  
  
	 } catch (NotAuthorizedException e) {

	  }
	 return defaultRespone;
  
 }



 @PUT
 @Path("/{token}/password")
 public Response passwordUser(

  @PathParam("token") String token,
  Account user2

 ) {
  Response response = defaultRespone;


  try {



   String Email = "Email";
   String UserPassword = "UserPassword";

   String NewPassword = user2.getUserPassword();


   Map < String, String > credentials = tokenUtils.decrypt(token);


   String Email2 = credentials.get(Email);
   String UserPassword2 = credentials.get(UserPassword);

   tokenUtils.check(new Account(Email2, UserPassword2), dao);

   new Thread(() -> {

    dao.changePassword(Email2, UserPassword2, NewPassword);

   }).start();

   String message = "Successfull";

   Response successResponse = Response.ok(message)
    .build();

   response = successResponse; //change response 


  } catch (NotAuthorizedException e) {

  }


  return response;




 }



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
 ) {
  //define default response return when error
  String failedResponeMessage = "Login credentials were invalide";

  Response defaultRespone = Response.serverError()
   .entity(failedResponeMessage)
   .build();

  Response response = defaultRespone; //return this response unless changed

  try {

   tokenUtils.check(user, dao);

   String token = tokenUtils.create(user);

   Response successResponse = Response.ok(new TokenBody(token), MediaType.APPLICATION_JSON) //Initialize success response and pass the token

    .build();

   response = successResponse; //change response 

  } catch (NotAuthorizedException e) {
   //do something different or customize the response 
  }






  return response;
 }

}