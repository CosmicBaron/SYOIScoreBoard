import time, datetime, math
from selenium import webdriver
from fetch import getall

chromepath = "~/home/christopher/CodeProjects/SYOIScoreBoard/chromedriver"

htmindex = \
f"""
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>SYIC Scoreboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>

<body>
<h1>SYIC Scoreboard</h1>
<p><i>Last updated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</i></p>

"""

htmending = \
"""
<p><i>Tool created by CosmicBaron</i></p>
</body>
</html>

"""

def sumuser(scores: dict):
    usersum = {}
    for prob in scores:
        # print(prob)
        for user, score in prob.items():
            usersum[user] = usersum.get(user, 0) + score
    finalsum = dict(sorted(usersum.items(), key=lambda item: item[1], reverse=True))
    print(finalsum)
    return finalsum

def addrank(scores):
    rankedsum = {}
    sortedsum = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    currank = 0
    lastscore = None
    rankcounter = 0  # To handle ties

    for name, score in sortedsum:
        rankcounter += 1
        if score != lastscore:
            currank = rankcounter
        rankedsum[name] = [currank, score]
        lastscore = score

    return rankedsum

def maketable(usersum: dict):
    table = \
    """
    <div class="scoreboard-container">
    """
    for i in range(int(math.ceil(len(usersum)/8))):
        usersumm = dict(list(usersum.items())[8*i:8+8*i])
        table += """
        <table>
        <tr>
            <th>Rank</th>
            <th>Contestant</th>
            <th>Score</th>
        </tr>
        """
        for k, v in usersumm.items():
            table += \
            f"""
            <tr>
                <td>{v[0]}</td>
                <td>{k}</td>
                <td>{v[1]}</td>
            </tr>
            """
        table += \
        """
        </table>
        """
    table += \
    """
    </div>
    """
    return table

def write():
    with open("index.html", "w") as f:
        page = htmindex + maketable(addrank(sumuser(getall()))) + htmending
        f.write(page)

def main():
    driver = webdriver.Firefox()
    driver.get("http://0.0.0.0:8000")
    while True:
        write()
        driver.refresh()
        time.sleep(20)

if __name__ == "__main__":
    main()