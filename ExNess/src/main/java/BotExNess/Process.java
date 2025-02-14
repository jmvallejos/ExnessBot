package BotExNess;

import java.util.logging.Logger;

public class Process {
	Logger _logger;
	
	public void Execute() {
		try{
			Init();
		}catch(Exception ex) {
			_logger.info(ex.getMessage());
		}
	}
	
	private void Init() {
		_logger = Logger.getLogger("");
		_logger.info("Test");
		_logger.info("Test");
	}
}
