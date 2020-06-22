package nl.Ipsen5Server.Domain;

public class Colleague {
	private String Email;
	private String UserPassword;
	private String UserType;

	public Colleague(String email, String userPassword, String userType) {
		super();
		this.Email = email;
		this.UserPassword = userPassword;
		this.UserType = userType;
	}

	public String getEmail() {
		return Email;
	}

	public void setEmail(String email) {
		Email = email;
	}

	public String getUserPassword() {
		return UserPassword;
	}

	public void setUserPassword(String userPassword) {
		UserPassword = userPassword;
	}

	public String getUserType() {
		return UserType;
	}

	public void setUserType(String userType) {
		UserType = userType;
	}
}
