package nl.Ipsen5Server.Domain;

public class ContactPerson {
	private String Name;
	private String SendMessage;
	private String Description;
	private String SocialMedia;
	private String UserName;

	public ContactPerson(String Name, String SendMessage, String Description, String SocialMedia, String UserName) {
		super();
		this.Name = Name;
		this.SendMessage = SendMessage;
		this.Description = Description;
		this.SocialMedia = SocialMedia;
		this.UserName = UserName;
	}

	public ContactPerson() {

	}

	public String getName() {
		return Name;
	}

	public void setName(String name) {
		Name = name;
	}

	public String getSendMessage() {
		return SendMessage;
	}

	public void setSendMessage(String sendMessage) {
		SendMessage = sendMessage;
	}

	public String getDescription() {
		return Description;
	}

	public void setDescription(String description) {
		Description = description;
	}

	public String getSocialMedia() {
		return SocialMedia;
	}

	public void setSocialMedia(String socialMedia) {
		SocialMedia = socialMedia;
	}

	public String getUserName() {
		return UserName;
	}

	public void setUserName(String userName) {
		UserName = userName;
	}
}
