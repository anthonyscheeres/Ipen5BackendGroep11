package nl.Ipsen5Server.Domain;

public class Account {
	 private String Email;
	    private String UserPassword;
		public Account(String Email, String UserPassword) {
			super();
			this.Email = Email;
			this.UserPassword = UserPassword;
		}
		
		public Account() {
			
		}

		public String getEmail() {
			return Email;
		}

		public void setEmail(String Email) {
			this.Email = Email;
		}

		public String getUserPassword() {
			return UserPassword;
		}

		public void setUserPassword(String UserPassword) {
			this.UserPassword = UserPassword;
		}
		
	    
}
