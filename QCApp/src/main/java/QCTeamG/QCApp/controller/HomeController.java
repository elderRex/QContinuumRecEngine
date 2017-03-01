package QCTeamG.QCApp.controller;

import java.security.Principal;
import java.util.List;
import java.util.Locale;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.AutowireCapableBeanFactory;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import com.google.gson.Gson;

import QCTeamG.QCApp.controller.SessionController;
import QCTeamG.QCApp.dao.UsersDAO;
import QCTeamG.QCApp.entities.UsersEntity;

/**
 * Sample controller for going to the home page with a message
 */
@Controller
public class HomeController {
	
	private @Autowired AutowireCapableBeanFactory beanFactory;
	
	@Autowired
	UsersDAO userDAO;

	private static final Logger logger = LoggerFactory
			.getLogger(HomeController.class);

	/**
	 * Selects the home page and populates the model with a message
	 */
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home(Model model) {
		logger.info("Welcome home!");
		model.addAttribute("controllerMessage",
				"This is the message from the controller!");
		return "home";
	}
	
	
	@Transactional
	@RequestMapping(value = "get_all_user_data", method = RequestMethod.GET,produces={"application/xml", "application/json"})
	public @ResponseBody String getAllUserData(Locale locale, Model model) {
		
		List<UsersEntity> all_user_data = (List<UsersEntity>)userDAO.getAllUsers();
		Gson gson = new Gson();
		String user_data_list = gson.toJson(all_user_data);
		
//		for (UsersEntity ue : all_user_data) {
//			//List<UserReviewsList> revs =
//			//String user_reviews_list = gson.toJson(luse);
//			
//			JSONObject jo = new JSONObject();
//			jo.put("all_reviews", reviews_list);
//
//			ls.add(jo.toString());
//		}

		return user_data_list.toString();
	

	}
}