
package nl.Ipsen5Server.Service;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.jsonwebtoken.JwtBuilder;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Domain.Account;
import nl.Ipsen5Server.Interfaces.Authorisation;
import org.joda.time.LocalDateTime;

import javax.ws.rs.NotAuthorizedException;
import java.util.HashMap;
import java.util.Map;


/**
*
* @author Anthony Scheeres
*
*/
public class Token implements Authorisation{
	private final String secretKey = "avgsgrethsbnyeastbcbIWHEHHGBWUYEBCEFJHTGBWGBWB2GYNBRGFBDDHDHREHFDJEZMJKMSVBHHnhdebrhbchrbmxjrufsncghrbfIverysecredapikey";
	private final SignatureAlgorithm signatureAlgorithm = SignatureAlgorithm.HS512;
	private final String Email  = "Email";
	private final String UserPassword= "UserPassword";
	private final String CreateDate = "CreateDate";
	
    /**
    *
    * @author Anthony Scheeres
    *
    */
	@Override
	public String create(Account user ){
		Map<String, Object> tokenData = new HashMap<String, Object>();
        tokenData.put(Email, user.getEmail());
        tokenData.put(UserPassword, user.getUserPassword());			//put values in the hashmap
        tokenData.put(CreateDate, LocalDateTime.now());
        
        
        JwtBuilder jwtBuilder = Jwts.builder();
        jwtBuilder.setClaims(tokenData);
    	
      
        
        String token = jwtBuilder.signWith(signatureAlgorithm, secretKey).compact(); //encrypt data
        return token; 
	}
	
    /**
    *
    * @author Anthony Scheeres
    *
    */
	@Override
	public void check(Account user, UserDAO dao) throws NotAuthorizedException {
		
		
    	int true_ = 1; //in mariadb 1 is true and 0 false
    	
        int isAutherised = dao.loginByEmailAndPassword(user.getEmail(), user.getUserPassword()); //check credentials in database
        
        if (isAutherised!=true_) { 
        	
        	String message = "Wrong username or password";
        	
        	throw new NotAuthorizedException(message);
        	
        }
		
		
	}
	
    /**
    *
    * @author Anthony Scheeres
    *
    */
	@Override
	public Map<String, String> decrypt(String token) {
	
		
		Object serializedObjects = Jwts.parser().setSigningKey(secretKey ).parseClaimsJws(token).getBody();  
		Map<String, String> response;
		
		 ObjectMapper oMapper = new ObjectMapper();
		
		response = oMapper.convertValue(serializedObjects, HashMap.class);
		
		return response;
	}
	
	
	
	
}

