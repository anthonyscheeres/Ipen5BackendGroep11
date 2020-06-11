package nl.Ipsen5Server.Presentation;

import nl.Ipsen5Server.Interfaces.Authorisation;
import nl.Ipsen5Server.Interfaces.InstagramBot;
import nl.Ipsen5Server.Interfaces.KikBot;
import nl.Ipsen5Server.Service.Token;

public class PlatformResource {
	  Authorisation a;
      InstagramBot i ;
      KikBot k;
      
      
      
	public PlatformResource(Authorisation a, InstagramBot i, KikBot k) {
		super();
		this.a = a;
		this.i = i;
		this.k = k;
	}
      
      
      
}
