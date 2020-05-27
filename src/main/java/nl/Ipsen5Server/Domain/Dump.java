package nl.Ipsen5Server.Domain;

public class Dump {
	private String UID;
	private String site;	
	private String date;	
	private String user;	
	private String email;	
	private String partial_IP;	
	private String genoemde_social_media;	
	private String title;
	private String message;
	
	
	public Dump(String uID, String site, String date, String user, String email, String partial_IP,
			String genoemde_social_media, String title, String message) {
		super();
		UID = uID;
		this.site = site;
		this.date = date;
		this.user = user;
		this.email = email;
		this.partial_IP = partial_IP;
		this.genoemde_social_media = genoemde_social_media;
		this.title = title;
		this.message = message;
	}
	
	public Dump() {
		super();
	}
	public String getUID() {
		return UID;
	}


	
	public String getSite() {
		return site;
	}
	
	public String getDate() {
		return date;
	}

	public String getUser() {
		return user;
	}
	
	public String getEmail() {
		return email;
	}

	public String getPartial_IP() {
		return partial_IP;
	}

	public String getGenoemde_social_media() {
		return genoemde_social_media;
	}

	public String getTitle() {
		return title;
	}
	
	public String getMessage() {
		return message;
	}
	

	
	
}
