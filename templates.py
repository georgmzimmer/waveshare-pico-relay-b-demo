def index(relays):
    # header portion, uses curly braces but we dont want to interpret as f string.
    template = """
<html>
<head><title>Pico Relay B</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        table {
            margin: auto
        }

        h1 {
            color: #0F3376;
            padding: 2vh;
        }

        p {
            font-size: 1.5rem;
        }

        .button {
            display: inline-block;
            background-color: #e7bd3b;
            border: none;
            border-radius: 4px;
            color: white;
            padding: 8px 8px;
            text-decoration: none;
            font-size: 30px;
            margin: 2px;
            cursor: pointer;
        }

        .button2 {
            background-color: #4286f4;
        }</style>
</head>
"""
    template += f"""
<body><h1>Pico Relay B</h1>
<div>
    <form method="POST">
    <table>
    <tr><td>
    <table>
        <tr>
            <th>Channel</th>
            <th>Pin</th>
            <th>State</th>
        </tr>
        <tr>
            <td>1</td>
            <td>GPIO {relays.channel1.pin}</td>
            <td>
                <input name="channel1" type="checkbox" value="1" {relays.channel1.checked()}/>
            </td>
        </tr>
        <tr>
            <td>2</td>
            <td>GPIO {relays.channel2.pin}</td>
            <td>
                <input name="channel2" type="checkbox" value="1" {relays.channel2.checked()}/>
            </td>
        </tr>
        <tr>
            <td>3</td>
            <td>GPIO {relays.channel3.pin}</td>
            <td>
                <input name="channel3" type="checkbox" value="1" {relays.channel3.checked()}/>
            </td>
        </tr>
        <tr>
            <td>4</td>
            <td>GPIO {relays.channel4.pin}</td>
            <td>
                <input name="channel4" type="checkbox" value="1" {relays.channel4.checked()}/>
            </td>
        </tr>
        <tr>
            <td>5</td>
            <td>GPIO {relays.channel5.pin}</td>
            <td>
                <input name="channel5" type="checkbox" value="1" {relays.channel5.checked()}/>
            </td>
        </tr>
        <tr>
            <td>6</td>
            <td>GPIO {relays.channel6.pin}</td>
            <td>
                <input name="channel6" type="checkbox" value="1" {relays.channel6.checked()}/>
            </td>
        </tr>
        <tr>
            <td>7</td>
            <td>GPIO {relays.channel7.pin}</td>
            <td>
                <input name="channel7" type="checkbox" value="1" {relays.channel7.checked()}/>
            </td>
        </tr>
        <tr>
            <td>8</td>
            <td>GPIO {relays.channel8.pin}</td>
            <td>
                <input name="channel8" type="checkbox" value="1" {relays.channel8.checked()}/>
            </td>
        </tr>
    </table>
    </td>
    </tr>
    </table>
    <button class="button" type="submit">Submit</button>
    </form>
    
</div>
</body>
</html>
"""
    return template.strip().replace("   ", " ").replace("  ", " ").replace("  ", " ")

