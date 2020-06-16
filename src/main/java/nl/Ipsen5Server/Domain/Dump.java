package nl.Ipsen5Server.Domain;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
*
* @author Anthony Scheeres
*
*/
public class Dump {

	
	@JsonProperty("UID")
	public String UID; 
	
	@JsonProperty("user")
	public String user; 
	
	@JsonProperty("partial IP")
	public String partial_IP;	
	
	@JsonProperty("genoemde social media")
	public  String genoemde_social_media;
	
	@JsonProperty("message")
	public String message;

	@JsonProperty("email")
public String email;
	
	@JsonProperty("title")
	public String title ;
	
	@JsonProperty("date")
	public String date;
	
	@JsonProperty("site")
	public String site;




	public Dump(String uID, String user, String partial_IP, String genoemde_social_media, String message, String email,
			String title, String date, String site) {
		super();
		UID = uID;
		this.user = user;
		this.partial_IP = partial_IP;
		this.genoemde_social_media = genoemde_social_media;
		this.message = message;
		this.email = email;
		this.title = title;
		this.date = date;
		this.site = site;
	}




	public Dump() {
		super();
	}




	public String getTitle() {
		return title;
	}



	@JsonProperty("title")
	public void setTitle(String title) {
		this.title = title;
	}




	public String getDate() {
		return date;
	}



	@JsonProperty("date")
	public void setDate(String date) {
		this.date = date;
	}




	public String getSite() {
		return site;
	}



	@JsonProperty("site")
	public void setSite(String site) {
		this.site = site;
	}




	public String getEmail() {
		return email;
	}



	@JsonProperty("email")
	public void setEmail(String email) {
		this.email = email;
	}




	public String getUID() {
		return UID;
	}




	@JsonProperty("UID")
	public void setUID(String uID) {
		UID = uID;
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
