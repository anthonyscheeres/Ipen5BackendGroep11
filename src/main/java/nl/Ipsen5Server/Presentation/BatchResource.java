package nl.Ipsen5Server.Presentation;

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
	
	
	//test token
	//token = "eyJhbGciOiJIUzUxMiJ9.eyJFbWFpbCI6Imsud2Fra2VybWFubUBtZWRlcndlcmtlci5ja20ubmwiLCJVc2VyUGFzc3dvcmQiOiJkb2VlZW5kYW5zamUiLCJDcmVhdGVEYXRlIjp7InllYXIiOjIwMjAsImRheU9mTW9udGgiOjI3LCJkYXlPZldlZWsiOjMsImRheU9mWWVhciI6MTQ4LCJlcmEiOjEsInllYXJPZkNlbnR1cnkiOjIwLCJjZW50dXJ5T2ZFcmEiOjIwLCJ3ZWVrT2ZXZWVreWVhciI6MjIsIndlZWt5ZWFyIjoyMDIwLCJ5ZWFyT2ZFcmEiOjIwMjAsIm1pbnV0ZU9mSG91ciI6NSwiaG91ck9mRGF5IjoxNCwibW9udGhPZlllYXIiOjUsImNocm9ub2xvZ3kiOnsiem9uZSI6eyJmaXhlZCI6dHJ1ZSwiaWQiOiJVVEMifX0sIm1pbGxpc09mU2Vjb25kIjozOTIsIm1pbGxpc09mRGF5Ijo1MDc0MzM5Miwic2Vjb25kT2ZNaW51dGUiOjQzLCJmaWVsZHMiOlt7ImxlbmllbnQiOmZhbHNlLCJyYW5nZUR1cmF0aW9uRmllbGQiOm51bGwsImxlYXBEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwibWluaW11bVZhbHVlIjotMjkyMjc1MDU0LCJtYXhpbXVtVmFsdWUiOjI5MjI3ODk5MywiZHVyYXRpb25GaWVsZCI6eyJ1bml0TWlsbGlzIjozMTU1Njk1MjAwMCwicHJlY2lzZSI6ZmFsc2UsIm5hbWUiOiJ5ZWFycyIsInR5cGUiOnsibmFtZSI6InllYXJzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sIm5hbWUiOiJ5ZWFyIiwidHlwZSI6eyJyYW5nZUR1cmF0aW9uVHlwZSI6bnVsbCwiZHVyYXRpb25UeXBlIjp7Im5hbWUiOiJ5ZWFycyJ9LCJuYW1lIjoieWVhciJ9LCJzdXBwb3J0ZWQiOnRydWV9LHsibGVuaWVudCI6ZmFsc2UsInJhbmdlRHVyYXRpb25GaWVsZCI6eyJ1bml0TWlsbGlzIjozMTU1Njk1MjAwMCwicHJlY2lzZSI6ZmFsc2UsIm5hbWUiOiJ5ZWFycyIsInR5cGUiOnsibmFtZSI6InllYXJzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sImxlYXBEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwibWluaW11bVZhbHVlIjoxLCJtYXhpbXVtVmFsdWUiOjEyLCJkdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjI2Mjk3NDYwMDAsInByZWNpc2UiOmZhbHNlLCJuYW1lIjoibW9udGhzIiwidHlwZSI6eyJuYW1lIjoibW9udGhzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sIm5hbWUiOiJtb250aE9mWWVhciIsInR5cGUiOnsicmFuZ2VEdXJhdGlvblR5cGUiOnsibmFtZSI6InllYXJzIn0sImR1cmF0aW9uVHlwZSI6eyJuYW1lIjoibW9udGhzIn0sIm5hbWUiOiJtb250aE9mWWVhciJ9LCJzdXBwb3J0ZWQiOnRydWV9LHsicmFuZ2VEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjI2Mjk3NDYwMDAsInByZWNpc2UiOmZhbHNlLCJuYW1lIjoibW9udGhzIiwidHlwZSI6eyJuYW1lIjoibW9udGhzIn0sInN1cHBvcnRlZCI6dHJ1ZX0sIm1pbmltdW1WYWx1ZSI6MSwibWF4aW11bVZhbHVlIjozMSwibGVuaWVudCI6ZmFsc2UsInVuaXRNaWxsaXMiOjg2NDAwMDAwLCJkdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwibmFtZSI6ImRheU9mTW9udGgiLCJ0eXBlIjp7InJhbmdlRHVyYXRpb25UeXBlIjp7Im5hbWUiOiJtb250aHMifSwiZHVyYXRpb25UeXBlIjp7Im5hbWUiOiJkYXlzIn0sIm5hbWUiOiJkYXlPZk1vbnRoIn0sInN1cHBvcnRlZCI6dHJ1ZSwibGVhcER1cmF0aW9uRmllbGQiOm51bGx9LHsicmFuZ2VEdXJhdGlvbkZpZWxkIjp7InVuaXRNaWxsaXMiOjg2NDAwMDAwLCJwcmVjaXNlIjp0cnVlLCJuYW1lIjoiZGF5cyIsInR5cGUiOnsibmFtZSI6ImRheXMifSwic3VwcG9ydGVkIjp0cnVlfSwicmFuZ2UiOjg2NDAwMDAwLCJtYXhpbXVtVmFsdWUiOjg2Mzk5OTk5LCJsZW5pZW50IjpmYWxzZSwidW5pdE1pbGxpcyI6MSwibWluaW11bVZhbHVlIjowLCJkdXJhdGlvbkZpZWxkIjp7Im5hbWUiOiJtaWxsaXMiLCJ0eXBlIjp7Im5hbWUiOiJtaWxsaXMifSwic3VwcG9ydGVkIjp0cnVlLCJ1bml0TWlsbGlzIjoxLCJwcmVjaXNlIjp0cnVlfSwibmFtZSI6Im1pbGxpc09mRGF5IiwidHlwZSI6eyJyYW5nZUR1cmF0aW9uVHlwZSI6eyJuYW1lIjoiZGF5cyJ9LCJkdXJhdGlvblR5cGUiOnsibmFtZSI6Im1pbGxpcyJ9LCJuYW1lIjoibWlsbGlzT2ZEYXkifSwic3VwcG9ydGVkIjp0cnVlLCJsZWFwRHVyYXRpb25GaWVsZCI6bnVsbH1dLCJmaWVsZFR5cGVzIjpbeyJyYW5nZUR1cmF0aW9uVHlwZSI6bnVsbCwiZHVyYXRpb25UeXBlIjp7Im5hbWUiOiJ5ZWFycyJ9LCJuYW1lIjoieWVhciJ9LHsicmFuZ2VEdXJhdGlvblR5cGUiOnsibmFtZSI6InllYXJzIn0sImR1cmF0aW9uVHlwZSI6eyJuYW1lIjoibW9udGhzIn0sIm5hbWUiOiJtb250aE9mWWVhciJ9LHsicmFuZ2VEdXJhdGlvblR5cGUiOnsibmFtZSI6Im1vbnRocyJ9LCJkdXJhdGlvblR5cGUiOnsibmFtZSI6ImRheXMifSwibmFtZSI6ImRheU9mTW9udGgifSx7InJhbmdlRHVyYXRpb25UeXBlIjp7Im5hbWUiOiJkYXlzIn0sImR1cmF0aW9uVHlwZSI6eyJuYW1lIjoibWlsbGlzIn0sIm5hbWUiOiJtaWxsaXNPZkRheSJ9XSwidmFsdWVzIjpbMjAyMCw1LDI3LDUwNzQzMzkyXX19.ac7Z6S7LdOAiviKnruXdgM6VPgQ7P9wQn7vc6KQojX9VROL2OBppJVbd-nxBG1HssMa17LhWcqJfSTZfRyeScg";
	
	try {
	
	String Email  = "Email";
	String UserPassword= "UserPassword";
		
	
	  
	  
		Map<String, String> h = tokenUtils.decrypt(token)	;
		
				
				  Email = h.get(Email);		
				  UserPassword = h.get(UserPassword);
				
		//System.out.println(h.get(Token.Email)); //test if email is correct
		
		tokenUtils.check(new Account(Email, UserPassword), user);
		
	
		
		
		 new Thread(() -> {
	     	
	  
		
	for (Dump excelRow : excel) {
	
		
		dao.Insert(excelRow.getEmail(), 
				
				excelRow.getGenoemde_social_media(), 
				excelRow.getMessage(), 
				excelRow.getPartial_IP(), 
				excelRow.getSite(), 
				excelRow.getTitle(), 
				excelRow.getUID(), 
				excelRow.getUser()
			
				);
		
	}
	
		   	}).start();
	
	String message = "Successfully created"; 
	
	Response successResponse = Response.ok(message)                       //Initialize success response and pass the token
            .build();
	
	response = successResponse; //change response 
	
	
	}
	catch (NotAuthorizedException e) {
		//do something different or customize the response 
	}
	        
	
	
	
		return response ;
	}
    
}
