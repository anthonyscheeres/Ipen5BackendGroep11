package nl.Ipsen5Server.Main;


import java.util.EnumSet;

import javax.servlet.DispatcherType;
import javax.servlet.FilterRegistration;

import io.dropwizard.jdbi3.JdbiFactory;
import io.dropwizard.server.DefaultServerFactory;
import nl.Ipsen5Server.Data.MessageDAO;
import nl.Ipsen5Server.Data.UserDAO;
import nl.Ipsen5Server.Presentation.MessageResource;
import nl.Ipsen5Server.Interfaces.Authorisation;
import nl.Ipsen5Server.Presentation.UserResource;
import org.eclipse.jetty.servlets.CrossOriginFilter;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;
import org.jdbi.v3.core.Jdbi;

public class Main extends Application<Settings>{
	
	
    public static void main(String[] args) throws Exception {
        new Main().run(args);
    }
	

    @Override
    public void initialize(Bootstrap<Settings> bootstrap) {

    }
    

    @Override
    public void run(Settings settings, Environment environment) throws Exception {

        //standard database initalaizations
        final JdbiFactory factory = new JdbiFactory();
        final DefaultServerFactory serverFactory = (DefaultServerFactory) settings.getServerFactory();
        final Jdbi jdbi = factory.build(environment, settings.getDataSourceFactory(), "mariadb");

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
        
        //initialize DAO's for the resources
        final UserDAO userDAO = jdbi.onDemand(UserDAO.class);
        final MessageDAO messageDAO = jdbi.onDemand(MessageDAO.class);

        Authorisation a = null ; // forces you to use the interfaced method
        
        //Initialize new resources
        environment.jersey().register(new UserResource(userDAO, a) );
        environment.jersey().register(new MessageResource(messageDAO));

    }
}