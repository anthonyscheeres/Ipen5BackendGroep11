package nl.Ipsen5Server.Presentation;


import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;


import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.NotAuthorizedException;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;


import nl.Ipsen5Server.Data.BatchDAO;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;
import nl.Ipsen5Server.Domain.Dump;

import nl.Ipsen5Server.Interfaces.Authorisation;


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
 @GET
 @Path("/{token}/show")
 @Produces(MediaType.APPLICATION_JSON)
 public Dump[] showBatches(@PathParam("token") String token) {
  Dump[] response = null;

  try {

   String Email = "Email";
   String UserPassword = "UserPassword";

   Map < String, String > credentials = tokenUtils.decrypt(token);


   Email = credentials.get(Email);
   UserPassword = credentials.get(UserPassword);

   tokenUtils.check(new Account(Email, UserPassword), user);

   response = dao.SelectBatches();





  } catch (NotAuthorizedException e) {

  }

  return response;



 }

 /**
 *
 * @author Anthony Scheeres
 *
 */
@GET
@Path("/Batch")
@Produces(MediaType.APPLICATION_JSON)
public Dump[] selectBatches() {
	return dao.SelectBatchNames();
	
}

 /**
  *
  * @author Anthony Scheeres
  *
  */
 @GET
 @Path("/{token}/showBatch/{id}/")
 @Produces(MediaType.APPLICATION_JSON)
 public Dump[] selectBatchesById(@PathParam("token") String token, @PathParam("id") String id) {
  Dump[] response = null;

  try {

   String Email = "Email";
   String UserPassword = "UserPassword";

   Map < String, String > credentials = tokenUtils.decrypt(token);


   Email = credentials.get(Email);
   UserPassword = credentials.get(UserPassword);

   tokenUtils.check(new Account(Email, UserPassword), user);

   response = dao.SelectSpecificBatches(id);


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
 @Path("/{token}/upload/{bestandsNaam}")
 @Consumes(MediaType.APPLICATION_JSON)
 @Produces(MediaType.TEXT_PLAIN)
 public Response uploadDump(List<Dump> excel, @PathParam("token") String token, @PathParam("bestandsNaam") String bestandsNaam) {
  Response response = defaultRespone; //return this response unless changed


  try {

   String Email = "Email";
   String UserPassword = "UserPassword";

   Map < String, String > credentials = tokenUtils.decrypt(token);


   Email = credentials.get(Email);
   UserPassword = credentials.get(UserPassword);

   tokenUtils.check(new Account(Email, UserPassword), user);
   
   String message = "Successfully created";
   

   Response successResponse = Response.ok(message) //Initialize success response and pass the token
    .build();


   
   response = successResponse; //change response 
   
   
   
   
   try {

	      dao.InsertBatch(bestandsNaam);
	    

	     } catch (SQLException e) {

	    	 Response fillNameNotRightResponse = Response.serverError()
	    	  .entity(failedResponeMessage)
	    	  .build();
	    	 
	    	 response = fillNameNotRightResponse;
	    	 
	    	 return response; 
	    	 
	     }
   
   new Thread(() -> {

    for (Dump excelRow: excel) {
     try {


      try {
       dao.InsertPlatform(

        excelRow.getGenoemde_social_media()

       );
       
      } catch (SQLException e) {

    	  
      }

      
     try {

       dao.InsertContactPersoon(

        excelRow.getGenoemde_social_media(),
     
        excelRow.getUser());

      } catch (SQLException e) {

      }

      dao.InsertContact(

       excelRow.getGenoemde_social_media(),
       excelRow.getUser()

      );

      dao.UpdateInfo(

       excelRow.getPartial_IP(),
       excelRow.getMessage(),
       excelRow.getGenoemde_social_media(),
       excelRow.getUser()

      );

      dao.InsertContactBatch(

       excelRow.getUser(),
       excelRow.getGenoemde_social_media(),
       bestandsNaam

      );

    } catch (SQLException e) {
//this row failed to insert
     }
    }

   }).start();





   response = successResponse; //change response 


  } catch (NotAuthorizedException e) {
	  response = defaultRespone; //return this response unless changed

  }




  return response;
 }

}