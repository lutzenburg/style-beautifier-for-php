<?php
/**
 * Rate limit exceptin to handle rate limit exceptions from the twitter API
 * https://dev.twitter.com/rest/public/rate-limiting
 */
namespace Codebots\Plugin\Twitterbot\Lib;
use \Codebots\Plugin\Twitterbot\Lib as TwitterbotLib;
class RateLimitException extends \Exception {
	public $rateLimit;
	public $message;
	public $code;
	/**
	 * Custom constructor.
	 * Rate Limit object can be provided, if it isn't, it is initiliased within the exception to get information.
	 * @param Ratelimit  $rateLimit Rate limit object.
	 */
	public function __construct($rateLimit = null) {
		$this->message = "Rate limit exceeded";
		$this->code = 88;
		if($userLookupRemaining) {
			$this->rateLimits = $rateLimit;
			$this->cause($this->rateLimits);
		}
		parent::__construct($this->message, $this->code, $previous = null);
	}
	/**
	 * Custom String representation
	 */
	public function __toString() {
		return __CLASS__ . ": [{$this->code}]: {$this->message}\n
				For Owner with ID {$this->rateLimit->ownerId}\n
				\tUser Lookups Remaining {$this->rateLimit->userLookupRemaining}, resets on {$this->rateLimit->userLookupReset->getTimestamp()}\n";
	}
	/**
	 * Find out what rate limit was exceeded.
	 */
	public function cause($rateLimit) {
		// Let us see what our rate limits are at.
		$this->message = $this->message .  "\n" .
			'User Lookup remaining ' .(($rateLimit->userLookupRemaining) ? '[true]' : '[false]') .
			', resets at ';
		if($rateLimit->userLookupReset) {
			$this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->userLookupReset->getTimestamp());
		}
		$this->message = $this->message .  "\n" .
			'Follower Ids remaining ' .(($rateLimit->followersIdsRemaining) ? '[true]' : '[false]') .
			', resets at ';
		if($rateLimit->followersIdsReset) {
			$this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->followersIdsReset->getTimestamp());
		}
		$this->message = $this->message . "\n" .
			'Friends Ids remaining ' .(($rateLimit->friendsIdsRemaining) ? '[true]' : '[false]') .
			', resets at ';
		if($rateLimit->friendsIdsReset) {
			$this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->friendsIdsReset->getTimestamp());
		}
		$this->message = $this->message .  "\n" .
			'Status User timeline remaining ' .(($rateLimit->statusesUserTimelineRemaining) ? '[true]' : '[false]') .
			', resets at ';
		if($rateLimit->statusesUserTimelineReset) {
			$this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->statusesUserTimelineReset->getTimestamp());
		}
		$this->message = $this->message .  "\n" .
			'Status Retweet remaining ' .(($rateLimit->statusesRetweetRemaining) ? '[true]' : '[false]') .
			', resets at ';
		if($rateLimit->statusesRetweetReset) {
			$this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->statusesRetweetReset->getTimestamp());
		}
		$this->message = $this->message .  "\n" .
			'Friendship Create remaining ' .(($rateLimit->userFriendshipCreateRemaining) ? '[true]' : '[false]') .
			', resets at ';
		if($rateLimit->userFriendshipUpdated) {
			$this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->userFriendshipUpdated->getTimestamp());
		}
		$this->message = $this->message .  "\n" .
			'Friendship Destroy remaining ' .(($rateLimit->userFriendshipDestroyRemaining) ? '[true]' : '[false]') .
			', resets at ';
		if($rateLimit->userFriendshipUpdated) {
			$this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->userFriendshipUpdated->getTimestamp());
		}
	}
}
this->message = $this->message . date ( "Y-m-d H:i:s",
			$rateLimit->userFriendshipUpdated->getTimestamp());
		}
	}
}

}
