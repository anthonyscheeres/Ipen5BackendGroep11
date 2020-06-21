package nl.Ipsen5Server.Models;

public class SocialMediaUsers {
	public String username;
	public String platform;
	
	
	public SocialMediaUsers(String username, String platform) {
		super();
		this.username = username;
		this.platform = platform;
	}


	public SocialMediaUsers() {
		super();
	}


	public String getUsername() {
		return username;
	}


	public void setUsername(String username) {
		this.username = username;
	}


	public String getPlatform() {
		return platform;
	}


	public void setPlatform(String platform) {
		this.platform = platform;
	} 
	
	
	
	
}
