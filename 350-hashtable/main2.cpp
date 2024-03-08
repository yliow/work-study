#include <iomanip>
#include <iostream>
#include <cstring>
#include <sstream>
#include <string>
#include <openssl/evp.h>

bool sha256_hexdigest(const char * unhashed, size_t unhashed_length,
                   std::string & hashed)
{
    bool success = false;
    EVP_MD_CTX * context = EVP_MD_CTX_new();

    if (context != NULL)
    {
        if (EVP_DigestInit_ex(context, EVP_sha256(), NULL))
        {
            if (EVP_DigestUpdate(context,
                                 unhashed, unhashed_length))
            {
                unsigned char hash[EVP_MAX_MD_SIZE];
                unsigned int lengthOfHash = 0;
                if (EVP_DigestFinal_ex(context, hash, &lengthOfHash))
                {
                    std::stringstream ss;
                    for (unsigned int i = 0; i < lengthOfHash; ++i)
                    {
                        ss << std::hex << std::setw(2) << std::setfill('0')
                           << (int)hash[i];
                    }
                    hashed = ss.str();
                    success = true;
                }
            }
        }
        EVP_MD_CTX_free(context);
    }
    return success;
}

int main(int argc, char ** argv)
{
    char input[1024];
    std::string output;

    strcpy(input, (const char *)"hello world");
    if (sha256_hexdigest(input, strlen(input), output))
    {
        std::cout << "hello world: " << output << std::endl;
    }
    else
    {
        std::cout << "FAILURE!" << std::endl;
    }

    strcpy(input, (const char *)"hello worle");
    if (sha256_hexdigest(input, strlen(input), output))
    {
        std::cout << "hello worle: " << output << std::endl;
    }
    else
    {
        std::cout << "FAILURE!" << std::endl;
    }

    int x;
    x = 42;
    if (sha256_hexdigest((const char *)(&x), sizeof(int), output))
    {
        std::cout << x << ": " << output << std::endl;
    }
    else
    {
        std::cout << "FAILURE!" << std::endl;
    }

    x = 43;
    if (sha256_hexdigest((const char *)(&x), sizeof(int), output))
    {
        std::cout << x << ": " << output << std::endl;
    }
    else
    {
        std::cout << "FAILURE!" << std::endl;
    }

    double d;
    d = 3.1415;
    if (sha256_hexdigest((const char *)(&d), sizeof(double), output))
    {
        std::cout << d << ": " << output << std::endl;
    }
    else
    {
        std::cout << "FAILURE!" << std::endl;
    }

    d = 3.1414;
    if (sha256_hexdigest((const char *)(&d), sizeof(double), output))
    {
        std::cout << d << ": " << output << std::endl;
    }
    else
    {
        std::cout << "FAILURE!" << std::endl;
    }

    return 0;
}