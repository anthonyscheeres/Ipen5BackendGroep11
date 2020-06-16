package nl.Ipsen5Server.Domain;
/**
*
* @author Anthony Scheeres
*
*/
public class Dump {

	private String user; 
	private String partial_IP;	
	private String genoemde_social_media;
	private String message;

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

	public void setUser(String user) {
		this.user = user;
	}

	public String getPartial_IP() {
		return partial_IP;
	}

	public void setPartial_IP(String partial_IP) {
		this.partial_IP = partial_IP;
	}

	public String getGenoemde_social_media() {
		return genoemde_social_media;
	}

	public void setGenoemde_social_media(String genoemde_social_media) {
		this.genoemde_social_media = genoemde_social_media;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}




	
	
}
