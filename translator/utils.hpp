
#ifndef __UTILS__
#define __UTILS__

#include <string>
#include <map>


typedef std::map<std::string,std::string> strmap;

namespace utl
{
	std::string args2map( int argc, char** argv ,strmap &params);
	void str2map(const std::string &str ,strmap &params);
	bool exists(const strmap &params,const std::string param);
	std::string ParseRemTill(std::string &str,char sep,bool &found);
	std::string TakeParseTo(std::string &str,char sep);
	std::string	getTime();
	std::string	getDay();
	
	std::string remove_spaces(std::string &str);
	std::string remove_0x(std::string &str);
	void remove(const std::string &substr, std::string &str);
	
	void hextext2data(const std::string &str, uint8_t *data);
	std::string data2hextext(const uint8_t *data,int data_size);
}

#endif /*__UTILS__*/