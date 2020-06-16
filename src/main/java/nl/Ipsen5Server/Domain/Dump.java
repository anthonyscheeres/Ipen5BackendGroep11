package nl.Ipsen5Server.Domain;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
*
* @author Anthony Scheeres
*
*/
public class Dump {

	@JsonProperty("user")
	public String user; 
	
	@JsonProperty("partial IP")
	public String partial_IP;	
	
	@JsonProperty("genoemde social media")
	public  String genoemde_social_media;
	
	@JsonProperty("message")
	public String message;

	public Dump(String user, String partial_IP, String genoemde_social_media, String message) {
		super();
		this.user = user;
		
	
		this.partial_IP = partial_IP;
		this.genoemde_social_media = genoemde_social_media;
		this.message = message;
	}

	
	
	
	public Dump() {
		super();
	}




	public String getUser() {
		return user;
	}

	
	
	@JsonProperty("user")
	public void setUser(String user) {
		this.user = user;
	}

	public String getPartial_IP() {
		return partial_IP;
	}

	@JsonProperty("partial IP")
	public void setPartial_IP(String partial_IP) {
		this.partial_IP = partial_IP;
	}

	
	public String getGenoemde_social_media() {
		return genoemde_social_media;
	}
	@JsonProperty("genoemde social media")
	public void setGenoemde_social_media(String genoemde_social_media) {
		this.genoemde_social_media = genoemde_social_media;
	}

	public String getMessage() {
		return message;
	}
	@JsonProperty("message")
	public void setMessage(String message) {
		this.message = message;
	}




	
	
}
