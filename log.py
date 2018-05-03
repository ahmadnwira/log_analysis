#!/usr/bin/env python3
# log analysis look for popular artilces, author and days with errors > 1

import psycopg2

# queries
popular_articles = """
                    SELECT articles.title, count(*) AS visits
                    FROM articles JOIN log"
                    ON log.path = concat('/article/', articles.slug)
                    GROUP BY articles.title
                    ORDER BY visits DESC
                    LIMIT(3);
                """

popular_authors = """
                    SELECT authors.name, count(*) as views
                    FROM articles JOIN authors
                    ON articles.author = authors.id
                    JOIN log
                    ON log.path = concat('/article/', articles.slug)
                    WHERE log.status LIKE '200%'
                    GROUP BY authors.name
                    ORDER BY views DESC;
                """

error_rate = """
                SELECT day_errors.day, round(error*100.0/(requests), 2)
                as error_rate
                FROM day_errors JOIN day_requests
                ON day_errors.day=day_requests.day
                WHERE error*100.0/(requests) > 1 LIMIT(3)
            """


def get_data(query, dbName="news"):
    """
        @param query : string represent sql query
        @param dbName : database name dafault DB is news

        returns the query resluts
        * use select queries only
    """
    try:
        conn = psycopg2.connect("dbname=%s" % dbName)
    except:
        return 'couldn\'t connect to the database'

    cursor = conn.cursor()
    results = cursor.fetchall()
    conn.close()
    return results


# Display queries
def display(query, identifier):
    for col_a, col_b in get_data(query):
        print("{} - {} {}".format(col_a, col_b, identifier))


if __name__ == "__main__":
    display(popular_articles, 'views')
    print('-------------\n')
    display(popular_authors, 'views')
    print('-------------\n')
    display(error_rate, '%')
