import serial
import argparse
import parse
import logging

from waggle.plugin import Plugin, get_timestamp




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Plugin for Pushing Viasala WXT 2D anemometer data through WSN")

    parser.add_argument("--debug",
                        action="store_true",
                        dest='debug',
                        help="print debug logs"
                        )
    parser.add_argument("--device",
                        type=str,
                        dest='device',
                        default="/dev/ttyUSB0",
                        help="Serial device ID"
                        )
    parser.add_argument("--baudrate",
                        type=int,
                        dest='baud_rate',
                        default=38400,
                        help="Baudrate"
                        )
    parser.add_argument("--node-publish-interval",
                        default=1.0,
                        dest='node_interval',
                        type=float,
                        help="interval to publish data to node " +
                             "(negative values disable node publishing)"
                        )
    parser.add_argument("--beehive-publish-interval",
                        default=1.0,
                        dest='beehive_interval',
                        type=float,
                        help="interval to publish data to beehive " +
                             "(negative values disable beehive publishing)"
                        )
    args = parser.parse_args()


    #main(args)
