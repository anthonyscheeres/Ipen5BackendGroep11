package nl.Ipsen5Server.Presentation;

import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;
import nl.Ipsen5Server.Domain.User;

import org.joda.time.LocalDateTime;
import org.json.JSONObject;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import java.util.*;

@Path("/user")
public class UserResource {

    private UserDAO dao;
    private final String secretKey = "avgsgrethsbnyeastbcbIWHEHHGBWUYEBCEFJHTGBWGBWB2GYNBRGFBDDHDHREHFDJEZMJKMSVBHHnhdebrhbchrbmxjrufsncghrbfIverysecredapikey";
    
    
    public UserResource(UserDAO dao) {
        this.dao = dao;
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

    
    	String failedResponeMessage = "Login credentials were invalide";
    	
    	Response defaultRespone = Response.serverError()
                .entity(failedResponeMessage)
                .build();
    	
    	Response response = defaultRespone; //return this response unless changed
    	
    	int true_ = 1; //in mariadb 1 is true and 0 false
    	
        int isAutherised = dao.loginByEmailAndPassword(user.getEmail(), user.getUserPassword()); //check credentials in database
        
        if (isAutherised==true_) {
        	
        	Map<String, Object> tokenData = new HashMap<String, Object>();
            tokenData.put("Email", user.getEmail());
            tokenData.put("UserPassword", user.getUserPassword());			//put values in the hashmap
            tokenData.put("CreateDate", LocalDateTime.now());
            
            
            JwtBuilder jwtBuilder = Jwts.builder();
            jwtBuilder.setClaims(tokenData);
        	
          
            
            String token = jwtBuilder.signWith(SignatureAlgorithm.HS512, secretKey).compact(); //encrypt data
        	
        	Response successResponse = Response.ok() 
                    .entity(token)                       //intialize success response and pass the token
                    .build();
        	
        	response = successResponse; //change response 
        	
        }
        
        return response;
    }

}
