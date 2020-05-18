package nl.Ipsen5Server.Main;


import java.util.EnumSet;

import javax.servlet.DispatcherType;
import javax.servlet.FilterRegistration;

import io.dropwizard.jdbi3.JdbiFactory;
import io.dropwizard.server.DefaultServerFactory;
import org.eclipse.jetty.servlets.CrossOriginFilter;

import io.dropwizard.Application;
import io.dropwizard.Configuration;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
import org.jdbi.v3.core.Jdbi;

public class Main extends Application<Configuration>{
	
	
    public static void main(String[] args) throws Exception {
        new Main().run(new String[] { "server" });
    }
	

    @Override
    public void initialize(Bootstrap<Configuration> bootstrap) {
       
    }
    

    @Override
    public void run(Configuration configuration, Environment environment) throws Exception {

        //standard initalaizations
        final JdbiFactory factory = new JdbiFactory();
        final DefaultServerFactory serverFactory = (DefaultServerFactory) configuration.getServerFactory();
        final Jdbi jdbi = factory.build(environment, configuration.getDataSourceFactory(), "postgresql");

        //api prefix
        serverFactory.setApplicationContextPath("/");
        serverFactory.setJerseyRootPath("/api");

    	 // Enable CORS headers
        final FilterRegistration.Dynamic cors = environment.servlets().addFilter("CORS", CrossOriginFilter.class);
        
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