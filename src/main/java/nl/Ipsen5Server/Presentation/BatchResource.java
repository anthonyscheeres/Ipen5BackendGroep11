package nl.Ipsen5Server.Presentation;


import java.util.ArrayList;
import java.util.List;
import java.util.Map;


import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import nl.Ipsen5Server.Domain.Batch;
import nl.Ipsen5Server.Domain.Message;
import org.jdbi.v3.sqlobject.SqlObject;
import org.jdbi.v3.core.statement.UnableToExecuteStatementException;



import nl.Ipsen5Server.Data.BatchDAO;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;
import nl.Ipsen5Server.Domain.Dump;
import nl.Ipsen5Server.Interfaces.Authorisation;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;


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
     * @author Anthony Scheeres
     */
    public BatchResource(BatchDAO dao, Authorisation tokenUtils, UserDAO user) {
        super();
        this.dao = dao;
        this.tokenUtils = tokenUtils;
        this.user = user;
    }


    /**
     * @author Anthony Scheeres
     */
    @POST
    @Path("/{token}/upload/{bestandsNaam}")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.TEXT_PLAIN)
    public Response uploadDump(List<Dump> excel, @PathParam("token") String token, @PathParam("bestandsNaam") String bestandsNaam) {
        Response response = defaultRespone; //return this response unless changed



 @GET
 @Path("/all")
 @Produces(MediaType.APPLICATION_JSON)
 public Response getAllBatches() {
  List<Map<String, Object>> allBatches = dao.getAllBatches();

  if (allBatches == null) {
   throw new WebApplicationException(Response.Status.NOT_FOUND);
  }

  return Response.ok(allBatches, MediaType.APPLICATION_JSON).build();

 }


            String Email = "Email";
            String UserPassword = "UserPassword";

            Map<String, String> credentials = tokenUtils.decrypt(token);


 /**
  *
  * @author Anthony Scheeres
  *
  */
 @GET
 @Path("/{token}/showBatch/{id}/")
 @Produces(MediaType.APPLICATION_JSON)
 public List<Map<String, Object>> selectBatchesById(@PathParam("token") String token, @PathParam("id") String id) {
  List<Map<String, Object>> response = null;

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
 @GET
 @Path("/{token}/show")
 @Produces(MediaType.APPLICATION_JSON)
 public List<Map<String, Object>> showBatches(@PathParam("token") String token) {
  List<Map<String, Object>> response = null;

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
@Produces(MediaType.APPLICATION_JSON)
public List<Map<String, Object>> selectBatches() {
	return dao.SelectBatchNames();
	
}

 


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

	     } catch (UnableToExecuteStatementException e) {


                response = fillNameNotRightResponse;

                return response;

            }

            new Thread(() -> {

    for (Dump excelRow: excel) {
    

      try {
    	  
       dao.InsertPlatform(


                for (Dump excelRow : excel) {
                    try {


       );
       
      } catch (UnableToExecuteStatementException e) {

                        try {

                            dao.InsertPlatform(

                                    excelRow.getGenoemde_social_media()

                            );


      } catch (UnableToExecuteStatementException e) {

      }
     
     
     try {
      dao.InsertContact(



                        try {


                            dao.InsertContactPersoon(

                                    excelRow.getGenoemde_social_media(),

                                    excelRow.getUser());

                        } catch (SQLException e) {


                        }


      );
      
      
      
      
     } catch (UnableToExecuteStatementException e) {

     }
      
dao.UpdateInfo(

	       excelRow.getPartial_IP(),
	       excelRow.getMessage(),
	       excelRow.getGenoemde_social_media(),
	       excelRow.getUser()

	      );

    
    }
   


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