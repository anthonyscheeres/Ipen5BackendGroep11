package nl.Ipsen5Server.Main;


import java.util.EnumSet;

import javax.servlet.DispatcherType;
import javax.servlet.FilterRegistration;

import org.eclipse.jetty.servlets.CrossOriginFilter;

import io.dropwizard.Application;
import io.dropwizard.Configuration;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

public class Main extends Application<Configuration>{
	
	
		  public static void main(String[] args) throws Exception {
			  new Main().run(new String[] { "server" });
		  }
	
	
    /**
     * @author Anthony Scheeres
     */
    @Override
    public void initialize(Bootstrap<Configuration> bootstrap) {
       
    }
    
    
    /**
     * @author Anthony Scheeres
     */
    @Override
    public void run(Configuration configuration, Environment environment) throws Exception {
    
    	
    	 // Enable CORS headers
        final FilterRegistration.Dynamic cors =
            environment.servlets().addFilter("CORS", CrossOriginFilter.class);
        
        // Configure CORS parameters
        cors.setInitParameter("allowedOrigins", "*");
        cors.setInitParameter("allowedHeaders", "X-Requested-With,Content-Type,Accept,Origin");
        cors.setInitParameter("allowedMethods", "OPTIONS,GET,PUT,POST,DELETE,HEAD");
        
        // Add URL mapping
        cors.addMappingForUrlPatterns(EnumSet.allOf(DispatcherType.class), true, "/*");
        
        
        //Example on how to import a resource:
		//environment.jersey().register(new UserResource());

    }
}